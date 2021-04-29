
export interface Posts {
  userId: number;
  id: number;
  title: string;
  rating: number;
  topicId: number;
}

export interface Topics {
  userId: number;
  id: number;
  title: string;
  rating: number;
  topicId: number;
}
export interface User {
  username: string;
  password: string;
  firstName: string;
  lastName: string;
}
export interface AuthToken {
  token: string;
}
export interface User {
  username: string;
  password: string;
  firstName: string;
  lastName: string;
}
