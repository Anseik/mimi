import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    login: false,
    userId: null,
    email: '',
  },
  mutations: {
    logout(state) {
      state.login = false;
      state.userId = null;
      state.email = null;
    },
    login(state, data) {
      state.login = true;
      state.userId = data.id
      state.email = data.email;
    },
  },
  actions: {
    LOGOUT({ commit }) {
      commit("logout");
      localStorage.removeItem("mimi-authorization")
    },
    LOGIN({ commit }, data) {
      commit("login", data);
    },
  },
  modules: {
  }
})
