export class Product {
  marka: string;
  type?: number;
  typ?: number;
  price: number;
  name: string;
  ean: string;
  stock_count: number;
  id?: number;
  longDescription: string;
  image?: string;

  constructor(item:Product) {
    this.marka = item.marka;
    this.type = item?.type || item?.typ;
    this.price =item.price;
    this.name = item.name;
    this.ean = item.ean;
    this.stock_count = item.stock_count;
    this.id = item.id;
    this.longDescription = item.longDescription;
    this.image = undefined
  }
}

export const defaultProduct = new Product({
  marka: '',
  type: 1,
  price: 1,
  name: '',
  ean: '',
  stock_count: 1,
  id: undefined,
  longDescription: '',
  image: ''
})