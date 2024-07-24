<template>
    <div class="selector">
      <h2>Escolha a Estampa da Camisa</h2>
      <select v-model="selectedPrint" @change="updatePrint">
        <option v-for="print in prints" :key="print" :value="print">{{ print }}</option>
      </select>
    </div>
  </template>
  
  <script>
  import { ref } from 'vue';
  
  export default {
    name: 'PrintSelector',
    emits: ['update-print'], // Define os eventos que o componente pode emitir
    setup(props, { emit }) {
      const prints = ref(['Estampa 1', 'Estampa 2', 'Estampa 3']);
      const selectedPrint = ref(null);
  
      const updatePrint = () => {
        emit('update-print', selectedPrint.value);
      };
  
      return { prints, selectedPrint, updatePrint };
    }
  };
  </script>
  
  <style>
  .selector {
    margin-bottom: 20px;
  }
  
  .selector h2 {
    font-size: 1.2em;
    margin-bottom: 10px;
  }
  
  .selector select {
    padding: 8px;
    font-size: 1em;
    width: 100%;
  }
  </style>  