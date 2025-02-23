export class Customer {
  id?: number;
  first_name: string;
  last_name?: string;
  phone_number?: string;
  postal_code?: string;
  nip?: number;
  city?: string;
  street?: string;
  company_name?: string;

  constructor(customer: Customer) {
    this.id = customer.id;
    this.first_name = customer.first_name;
    this.last_name = customer.last_name;
    this.phone_number = customer.phone_number;
    this.postal_code = customer.postal_code;
    this.nip = customer.nip;
    this.city = customer.city;
    this.street = customer.street;
    this.company_name = customer.company_name;
  }
}

export const defaultCustomer = new Customer({
  id: undefined,
  first_name: '',
  last_name: '',
  phone_number: '',
  postal_code: '',
  nip: 1,
  city: '',
  street: '',
  company_name: '',
})