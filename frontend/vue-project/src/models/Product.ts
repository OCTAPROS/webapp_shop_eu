export class Product {
  brand_id: number;
  product_type_id: number;
  product_type?: string;
  price: number;
  name: string;
  ean: string;
  qty_on_stock?: number;
  id?: number;
  description: string;

  constructor(item:Product) {
    this.brand_id = item.brand_id;
    this.product_type_id = item?.product_type_id;
    this.product_type = item?.product_type
    this.price =item.price;
    this.name = item.name;
    this.ean = item.ean;
    this.qty_on_stock = item?.qty_on_stock;
    this.id = item.id;
    this.description = item.description;
  }
}

export const defaultProduct = new Product({
  brand_id: 1,
  product_type_id: 1,
  product_type: '',
  price: 1,
  name: '',
  ean: '',
  qty_on_stock: 2,
  id: undefined,
  description: ''
})