import axios from '@/plugins/axios';
import type { AxiosInstance } from 'axios';
import { Product } from '@/models/Product';
import { BASE_URL } from '@/main';

export class ProductService {
  private httpClient: AxiosInstance;

  constructor() {
    this.httpClient = axios.create({
      baseURL: `${BASE_URL}`,
      timeout: 5000,
    });
  }

  async getProducts(): Promise<Product[]> {
    try {
      console.log('BASE_URL', BASE_URL)
      const response = await this.httpClient.get<Product[]>('/products/?skip=0&limit=10'); //TODO paginacja
      console.log('response', response.data)
      return response.data.map((product: Product) =>
          new Product(product)
      );
    } catch (error) {
      console.error('Error fetching products:', error);
      throw new Error('Unable to fetch products');
    }
  }
}