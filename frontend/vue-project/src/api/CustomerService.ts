import axios from '@/plugins/axios';
import type { AxiosInstance } from 'axios';
import { Customer } from '@/models/Customer';
import { BASE_URL } from '@/main';

export class CustomerService {
  private httpClient: AxiosInstance;

  constructor() {
    this.httpClient = axios.create({
      baseURL: `${BASE_URL}`,
      timeout: 5000,
    });
  }

  async getCustomers(): Promise<Customer[]> {
    try {
      const response = await this.httpClient.get<Customer[]>('/customers/?skip=0&limit=10'); //TODO paginacja
      return response.data.map((product: Customer) =>
          new Customer(product)
      );
    } catch (error) {
      console.error('Error fetching products:', error);
      throw new Error('Unable to fetch products');
    }
  }
}