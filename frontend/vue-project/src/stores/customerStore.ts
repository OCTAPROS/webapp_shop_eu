// Utilities
import { defineStore } from 'pinia'
import { Customer } from '@/models/Customer'
import { CustomerService } from '@/api/CustomerService';


const customerService = new CustomerService();


export const useCustomerStore = defineStore('customer', {
  state: () => ({
    customers: [] as Customer[],
    isLoading: false,
    error: null as string | null,
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
  },

  getters: {
    availableCustomers(state) {
      return state.customers;
    },
  },
});