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

     addProduct(product: Product) {
      this.products.push({ ...product, id: Date.now() });
    },
    async deleteProduct(productId: number) {
      try{
        await productService.deleteProduct(productId)
        this.products = this.products.filter((p: Product) => p.id !== productId);
      } catch (err) {
        this.error = 'Nie udało się usunąć produktu.';
        console.error(err);
      }
    },
    async updateProduct(updatedProduct: Product) {
      try {
        const newProduct = await productService.editProduct(updatedProduct)
        const index = this.products.findIndex((p: Product) => p.id === newProduct.id);
        if (index !== -1) {
          this.products[index] = newProduct;
        }
      } catch (err) {
        this.error = 'Nie udało się zmienić produktu.';
        console.error(err);
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