<template>
  <div>
    <CalendarWidget/>
  </div>
</template>

<script>
import CalendarWidget from './components/CalendarWidget.vue'
export default {
  name: 'App',
  components: {
    CalendarWidget
  }
}
</script>

<style>
.container {
  max-width: 500px;
}
</style>