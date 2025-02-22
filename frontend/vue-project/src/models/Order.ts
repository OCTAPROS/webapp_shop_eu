
export type OrderRow = {
  product_id: number;
  quantity: number;
}


export class OrderReturn {
  status: string;
  date: string;

  constructor(item: OrderReturn) {
    this.status = item.status
    this.date = item.date
  }
}

export class Order {
  payment_method_id: number;
  delivery_method_id: number;
  order_rows: OrderRow[]


  constructor(item: Order) {
    this.payment_method_id = item?.payment_method_id;
    this.delivery_method_id =item.delivery_method_id;
    this.order_rows = item.order_rows;
  }
}

export const defaultOrder = new Order({
  payment_method_id: 0,
  delivery_method_id: 0,
  order_rows: [
    {
      product_id: 1,
      quantity: 1,
    }
  ],

})

