// Utilities
import { defineStore } from 'pinia'
import { Product } from '@/models/Product'

type ProductInCart = { product: Product, quantity: number, id: number}


export const useCartStore = defineStore('cart', {
  state: () => ({
    cart: JSON.parse(localStorage.getItem('cart') || '[]'),
  }),
  getters: {
    totalItems: (state) => state.cart.reduce((acc: number, item: ProductInCart) => acc + item.quantity, 0),
    totalPrice: (state) =>
      state.cart.reduce((acc: number, item: ProductInCart) => acc + item.quantity * item.price, 0),
    orderRows: (state) => state.cart.map((item: ProductInCart) => ({ 'quantity': item.quantity, 'product_id': item.id }))
  },
  actions: {
    addToCart(product: Product, quantity: number) {
      const existingItem = this.cart.find((item: Product) => item.id === product.id);
      if (existingItem) {
        existingItem.quantity += quantity;
      } else {
        this.cart.push({ ...product, quantity: quantity });
      }
      this.saveCart();
    },
    removeFromCart(productId: number) {
      this.cart = this.cart.filter((item: Product) => item.id !== productId);
      this.saveCart();
    },
    updateQuantity(productId: number, quantity: number) {
      const item = this.cart.find((item: Product) => item.id === productId);
      if (item && quantity > 0) {
        item.quantity = quantity;
      } else if (quantity === 0) {
        this.removeFromCart(productId);
      }
      this.saveCart();
    },
    saveCart() {
      localStorage.setItem('cart', JSON.stringify(this.cart));
    },
    clearCart() {
      this.cart = [];
      this.saveCart();
    },
  },
});