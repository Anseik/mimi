import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'
import jwt_decode from "jwt-decode";

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    login: false,
    user: null,
  },
  mutations: {
    logout(state) {
      state.login = false;
      state.user = null;
    },
    login(state, token) {
      let decode = jwt_decode(token);
      // console.log(decode)
      state.login = true;
      // console.log(state.login)
      state.user = decode.user
      // console.log(state.user)
    },
  },
  actions: {
    LOGOUT({ commit }) {
      commit("logout");
      localStorage.removeItem("mimi-authorization")
    },
    LOGIN({ commit }, token) {
      commit("login", token);
    },
  },
  modules: {
  },
  plugins: [
    createPersistedState()
  ]
})
