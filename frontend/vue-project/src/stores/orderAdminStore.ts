import { defineStore } from 'pinia'
import { Order, OrderReturn } from '@/models/Order';
import { OrderService } from '@/api/orderService';
import { OrderAdmin } from '@/models/OrderAdmin';


const orderService = new OrderService();


export const useOrderStore = defineStore('order', {
  state: () => ({
    orders: [] as OrderAdmin[],
    isLoading: false,
    error: null as string | null,
    orderResponse: {} as OrderReturn
  }),

  actions: {
    async fetchCustomers(skip: number, limit: number) {
      this.isLoading = true;
      this.error = null;

      try {
        const orders = await orderService.getOrder(skip, limit);
        this.orders = orders;
      } catch (err) {
        this.error = 'Nie udało się pobrać produktów.';
        console.error(err);
      } finally {
        this.isLoading = false;
      }
    },
    
  },

  getters: {
    availableOrders(state) {
      return state.orders;
    },
  },
});