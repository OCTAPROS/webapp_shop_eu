import axios from '@/plugins/axios';
import type { AxiosInstance } from 'axios';
import { Dict } from '@/models/Dict';
import { BASE_URL } from '@/main';

export class DictService {
  private httpClient: AxiosInstance;

 constructor() {
    this.httpClient = axios 
  }

  async getBrand(): Promise<Dict[]> {
    try {
      const response = await this.httpClient.get<Dict[]>('/dicts/BRAND'); //TODO paginacja
      return response.data.map((product: Dict) =>
        new Dict(product)
      );
    } catch (error) {
      console.error('Error fetching products:', error);
      throw new Error('Unable to fetch products');
    }
  }

  async getDELIVERY_METHOD(): Promise<Dict[]> {
    try {
      const response = await this.httpClient.get<Dict[]>('/dicts/DELIVERY_METHOD'); //TODO paginacja
      return response.data.map((product: Dict) =>
          new Dict(product)
      );
    } catch (error) {
      console.error('Error fetching products:', error);
      throw new Error('Unable to fetch products');
    }
  }

  async getPAYMENT_METHOD(): Promise<Dict[]> {
    try {
      const response = await this.httpClient.get<Dict[]>('/dicts/PAYMENT_METHOD'); //TODO paginacja
      return response.data.map((product: Dict) =>
          new Dict(product)
      );
    } catch (error) {
      console.error('Error fetching products:', error);
      throw new Error('Unable to fetch products');
    }
  }

  async getPRODUCT_TYPE(): Promise<Dict[]> {
    try {
      const response = await this.httpClient.get<Dict[]>('/dicts/PRODUCT_TYPE'); //TODO paginacja
      return response.data.map((product: Dict) =>
          new Dict(product)
      );
    } catch (error) {
      console.error('Error fetching products:', error);
      throw new Error('Unable to fetch products');
    }
  }

  async getSTATUS(): Promise<Dict[]> {
    try {
      const response = await this.httpClient.get<Dict[]>('/dicts/STATUS'); //TODO paginacja
      return response.data.map((product: Dict) =>
          new Dict(product)
      );
    } catch (error) {
      console.error('Error fetching products:', error);
      throw new Error('Unable to fetch products');
    }
  }
}

