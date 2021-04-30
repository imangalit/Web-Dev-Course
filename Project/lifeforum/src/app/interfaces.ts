
export interface Posts {
  id: number;
  description: string;
  name: string;
  topicId: number;
}
export interface Comments {
  id: number;
  description: string;
}

export interface Topics {
  id: number;
  title: string;
}
export interface User {
  username: string;
  password: string;
  firstName: string;
  lastName: string;
}
export interface AuthToken {
  token: string;
  expires: number;
}
export interface User {
  username: string;
  password: string;
  firstName: string;
  lastName: string;
}
