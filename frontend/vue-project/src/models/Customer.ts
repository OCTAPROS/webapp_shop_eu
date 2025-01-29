export class Customer {
  id?: number;
  name: string;
  last_name?: string;

  constructor(customer: Customer) {
    this.id = customer.id;
    this.name = customer.name;
    this.last_name = customer.last_name
  }
}

export const defaultCustomer = new Customer({
  id: undefined,
  name: '',
  last_name: ''
})