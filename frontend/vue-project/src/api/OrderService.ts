import instance from '@/plugins/axios';
import type { AxiosInstance } from 'axios';
import { OrderAdmin } from '@/models/OrderAdmin';

export class OrderService {
  private httpClient: AxiosInstance;

 constructor() {
    this.httpClient = instance 
  }

  async getOrder(skip:number, limit:number): Promise<OrderAdmin[]> {
    try {
      const response = await this.httpClient.get<OrderAdmin[]>(`/orders/?skip=${skip}&limit=${limit}`); //TODO paginacja
      return response.data.map((o: OrderAdmin) => new OrderAdmin(o));
    } catch (error) {
      console.error('Error fetching products:', error);
      throw new Error('Unable to fetch products');
    }
  }
}