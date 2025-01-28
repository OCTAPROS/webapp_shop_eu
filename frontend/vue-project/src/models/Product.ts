export class Product {
  marka: string;
  typ: number;
  price: number;
  name: string;
  ean: string;
  stock_count: number;
  id: number;
  longDescription: string;

  constructor(item:Product) {
    this.marka = item.marka;
    this.typ = item.typ;
    this.price =item.price;
    this.name = item.name;
    this.ean = item.ean;
    this.stock_count = item.stock_count;
    this.id = item.id;
    this.longDescription = item.longDescription;
  }
}