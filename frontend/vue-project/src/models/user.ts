export class User {
  customer_id?: number;
  email: string;
  id?: number;
  is_active: boolean;
  is_superuser: boolean;

  constructor(customer: User) {
    this.customer_id = customer.customer_id;
    this.email = customer.email;
    this.id = customer.id
    this.is_active = customer.is_active
    this.is_superuser = customer.is_superuser
  }
}

export const defaultUser = new User({
  customer_id: 1,
  email: '',
  id: 1,
  is_active: false,
  is_superuser: false,
})