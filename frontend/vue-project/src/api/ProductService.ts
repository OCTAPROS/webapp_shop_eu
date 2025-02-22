import axios from '@/plugins/axios';
import type { AxiosInstance } from 'axios';
import { Product } from '@/models/Product';
import { BASE_URL } from '@/main';

export class ProductService {
  private httpClient: AxiosInstance;

 constructor() {
    this.httpClient = axios 
  }

  async getProducts(skip:number, limit:number): Promise<Product[]> {
    try {
      const response = await this.httpClient.get<Product[]>(`/products/?skip=${skip}&limit=${limit}`); //TODO paginacja
      return response.data.map((product: Product) =>
          new Product(product)
      );
    } catch (error) {
      console.error('Error fetching products:', error);
      throw new Error('Unable to fetch products');
    }
  }

  async editProduct(product: Product): Promise<Product> {
    try {
      console.log('ProductService product: ', product)
      const response = await this.httpClient.put<Product>(`/products/${product.id}`, product);
      return response.data
    } catch (error) {
      console.error('Error fetching products:', error);
      throw new Error('Unable to fetch products');
    }
  }

  async addProduct(product: Product): Promise<Product> {
    try {
      console.log('ProductService product: ', product)
      const response = await this.httpClient.post<Product>(`/products/`, product);
      return response.data

    } catch (error) {
      console.error('Error fetching products:', error);
      throw new Error('Unable to fetch products');
    }
  }

  async deleteProduct(id: number): Promise<void> {
    try {
      const response = await this.httpClient.delete<Product>(`/products/${id}`);
      console.log('response', response.data)

    } catch (error) {
      console.error('Error fetching products:', error);
      throw new Error('Unable to fetch products');
    }
  }
}