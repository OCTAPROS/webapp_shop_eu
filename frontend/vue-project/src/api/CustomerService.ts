import axios from '@/plugins/axios';
import type { AxiosInstance } from 'axios';
import { Customer } from '@/models/Customer';
import { User } from '@/models/user';
import { Order, OrderReturn } from '@/models/Order';

export class CustomerService {
  private httpClient: AxiosInstance;

  constructor() {
    this.httpClient = axios 
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

  async me(): Promise<User> {
    try {
      const response = await this.httpClient.get<User>('/auth/me'); //TODO paginacja
      console.log('me', response.data)
      return new User (response.data)
    } catch (error) {
      console.error('Error fetching products:', error);
      throw new Error('Unable to fetch products');
    }
  }

  async order(data: Order): Promise<OrderReturn> {
    try {
      console.log('order send', data)
      const response = await this.httpClient.post<OrderReturn>('/orders', data); //TODO paginacja
      console.log('order response', response.data)
      return new OrderReturn(response.data)

    } catch (error) {
      console.error('Error fetching products:', error);
      throw new Error('Unable to fetch products');
    }
  }


}