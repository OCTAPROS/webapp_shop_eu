export class Dict {
  id?: number;
  dict_value: string;

  constructor(dict: Dict) {
    this.id = dict.id;
    this.dict_value = dict.dict_value;
  }
}

export const defaultDict = new Dict({
  id: undefined,
  dict_value: '',
})