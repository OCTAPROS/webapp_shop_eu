// Utilities
import { defineStore } from 'pinia'
import { Customer } from '@/models/Customer'
import { User, defaultUser } from '@/models/user'
import { CustomerService } from '@/api/CustomerService';
import { Order, OrderReturn } from '@/models/Order';


const customerService = new CustomerService();


export const useCustomerStore = defineStore('customer', {
  state: () => ({
    customers: [] as Customer[],
    isLoading: false,
    error: null as string | null,
    u: JSON.parse(localStorage.getItem('user') || '[]'),
    orderResponse: {} as OrderReturn
  }),

  actions: {
    async fetchCustomers() {
      this.isLoading = true;
      this.error = null;

      try {
        const customers = await customerService.getCustomers();
        this.customers = customers;
      } catch (err) {
        this.error = 'Nie udało się pobrać produktów.';
        console.error(err);
      } finally {
        this.isLoading = false;
      }
    },
    
    async fetchUser() {
      try {
        const a = await customerService.me();
        this.u = a
        localStorage.setItem('user', JSON.stringify(this.u));
      } catch (err) {
        this.error = 'Nie udało się pobrać.';
        console.error(err);
      } finally {
        this.isLoading = false;
      }
    },

    async order(data: Order) {
      try {
        const response = await customerService.order(data);
        this.orderResponse = response
      } catch (err) {
        this.error = 'Nie udało się pobrać.';
        console.error(err);
      } finally {
        this.isLoading = false;
      }
    }

  },

  getters: {
    availableCustomers(state) {
      return state.customers;
    },
    user(state) {
      return state.u;
    },
  },
});