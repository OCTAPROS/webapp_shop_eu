// Utilities
import { defineStore } from 'pinia'
import { Dict, defaultDict } from '@/models/Dict'
import { DictService } from '@/api/DictService';


const dictService = new DictService();


export const useDictStore = defineStore('Dict', {
  state: () => ({
    Dicts: [] as Dict[],
    isLoading: false,
    error: null as string | null,
    BRAND: [] as Dict[],
    DELIVERY_METHOD: [] as Dict[],
    PAYMENT_METHOD: [] as Dict[],
    PRODUCT_TYPE: [] as Dict[],
    STATUS: [] as Dict[],
  }),

  actions: {
    async fetchBRAND() {
      this.isLoading = true;
      this.error = null;
      try {
        const BRAND = await dictService.getBrand();
        this.BRAND.push(defaultDict)
        BRAND.map((item: Dict) => this.BRAND.push(item))
      } catch (err) {
        this.error = 'Nie udało się pobrać firm.';
        console.error(err);
      } finally {
        this.isLoading = false;
      }
    },

    async fetchDELIVERY_METHOD() {
      this.isLoading = true;
      this.error = null;

      try {
        const DELIVERY_METHOD = await dictService.getDELIVERY_METHOD();
        this.DELIVERY_METHOD.push(defaultDict)
        DELIVERY_METHOD.map((item: Dict) => this.DELIVERY_METHOD.push(item))
      } catch (err) {
        this.error = 'Nie udało się pobrać firm.';
        console.error(err);
      } finally {
        this.isLoading = false;
      }
    },

    async fetchPAYMENT_METHOD() {
      this.isLoading = true;
      this.error = null;

      try {
        const PAYMENT_METHOD = await dictService.getPAYMENT_METHOD();
        this.PAYMENT_METHOD = PAYMENT_METHOD;
      } catch (err) {
        this.error = 'Nie udało się pobrać firm.';
        console.error(err);
      } finally {
        this.isLoading = false;
      }
    },

    async fetchPRODUCT_TYPE() {
      this.isLoading = true;
      this.error = null;

      try {
        const PRODUCT_TYPE = await dictService.getPRODUCT_TYPE();
        this.PRODUCT_TYPE.push(defaultDict)
        PRODUCT_TYPE.map((item: Dict)=> this.PRODUCT_TYPE.push(item))
      } catch (err) {
        this.error = 'Nie udało się pobrać firm.';
        console.error(err);
      } finally {
        this.isLoading = false;
      }
    },

    async fetchSTATUS() {
      this.isLoading = true;
      this.error = null;

      try {
        const STATUS = await dictService.getSTATUS();
        this.STATUS = STATUS;
      } catch (err) {
        this.error = 'Nie udało się pobrać firm.';
        console.error(err);
      } finally {
        this.isLoading = false;
      }
    },
  },

  getters: {
    availableDicts(state) {
      return state.Dicts;
    },
    availableBrand(state) {
      return state.BRAND;
    },
    availableDELIVERY_METHOD(state) {
      return state.DELIVERY_METHOD;
    },
    availablePAYMENT_METHOD(state) {
      return state.PAYMENT_METHOD;
    },
    availablePRODUCT_TYPE(state) {
      return state.PRODUCT_TYPE;
    },
    availableSTATUS(state) {
      return state.STATUS;
    },
  },
});