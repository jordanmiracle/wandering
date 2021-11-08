import {createApp} from 'vue'
import App from './App.vue'
import VueCal from 'vue-cal'
import 'vue-cal/dist/vuecal.css'
import datePicker from 'vue-bootstrap-datetimepicker'

Vue.use(datePicker);

newVue({
    render: h => h(App)
}).$mount('#app')


export default {
    components: {VueCal},
    data: () => ({}),

}
createApp(App).mount('#app')
