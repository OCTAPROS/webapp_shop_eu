// Utilities
import { defineStore } from 'pinia'
import { Product } from '@/models/Product'
import { ProductService } from '@/api/ProductService';


const productService = new ProductService();


export const useProductStore = defineStore('product', {
  state: () => ({
    products: [] as Product[],
    isLoading: false,
    error: null as string | null,
  }),

  actions: {
    async fetchProducts() {
      this.isLoading = true;
      this.error = null;

      try {
        const products = await productService.getProducts();
        this.products = products;
      } catch (err) {
        this.error = 'Nie udało się pobrać produktów.';
        console.error(err);
      } finally {
        this.isLoading = false;
      }
    },
  },

  getters: {
    availableProducts(state) {
      return state.products;
    },


    sortedProductsByPrice(state) {
      return [...state.products].sort((a, b) => a.price - b.price);
    },
  },
});