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
    u: defaultUser,
    orderResponse: {}
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
        console.log(a)
        this.u = a
      } catch (err) {
        this.error = 'Nie udało się pobrać produktów.';
        console.error(err);
      } finally {
        this.isLoading = false;
      }
    },

    async order(data: Order) {
      try {
        const response = await customerService.order(data);
        console.log(response)
        this.orderResponse = response
      } catch (err) {
        this.error = 'Nie udało się pobrać produktów.';
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