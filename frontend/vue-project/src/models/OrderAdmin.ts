export class OrderAdmin {
  city: string;
  customer_id: number;
  first_name: string;
  id: number;
  last_name: string;
  order_number: number;
  order_status: string;
  order_value?: number; 
  payment_method: string;
  payment_method_id: number;
  phone_number: string;
  status_id: number;
  street: string;
  delivery_method: string;
  delivery_method_id: number;

  constructor(item: OrderAdmin) {
    this.city = item.city
    this.customer_id = item.customer_id
    this.first_name = item.first_name
    this.id = item.id
    this.last_name = item.last_name
    this.order_number = item.order_number
    this.order_status = item.order_status
    this.order_value = item.order_value
    this.payment_method = item.payment_method
    this.payment_method_id = item.payment_method_id
    this.phone_number = item.phone_number
    this.status_id = item.status_id
    this.street = item.street
    this.delivery_method = item.delivery_method
    this.delivery_method_id = item.delivery_method_id
  }
}

export const defaultOrder = new OrderAdmin({
  city: '',
  customer_id: 1,
  first_name: '',
  id: 1,
  last_name: '',
  order_number: 1,
  order_status:  '',
  order_value: 1,
  payment_method: '',
  payment_method_id: 1,
  phone_number: '',
  status_id: 1,
  street: '',
  delivery_method: '',
  delivery_method_id: 1
})
