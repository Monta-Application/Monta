// action - state management
import { REGISTER, LOGIN, LOGOUT } from './actions';

// types
import { AuthProps, AuthActionProps } from 'types/auth';

// initial state
export const initialState: AuthProps = {
  isAuthenticated: false,
  isLoading: false,
  isInitialized: false,
  user: null
};

// ==============================|| AUTH REDUCER ||============================== //

const auth = (state = initialState, action: AuthActionProps) => {
  switch (action.type) {
    case REGISTER: {
      const { user } = action.payload!;
      return {
        ...state,
        user
      };
    }
    case LOGIN: {
      const { user } = action.payload!;
      return {
        ...state,
        isAuthenticated: true,
        user
      };
    }
    case LOGOUT: {
      return {
        ...state,
        isAuthenticated: false,
        user: null
      };
    }
    default: {
      return { ...state };
    }
  }
};

export default auth;
