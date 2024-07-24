<template>
    <div class="selector">
      <h2>Escolha o Modelo da Camisa</h2>
      <select v-model="selectedShirt" @change="updateShirtType">
        <option v-for="shirt in shirts" :key="shirt.id" :value="shirt">{{ shirt.name }}</option>
      </select>
    </div>
  </template>
  
  <script>
  import { ref, onMounted } from 'vue';
  
  export default {
    emits: ['update-shirt'],
    setup(props, { emit }) {
      const shirts = ref([]);
      const selectedShirt = ref(null);
      const shirtType = ref('');
  
      // Função para buscar camisas da API
      const fetchShirts = async () => {
        try {
          const response = await fetch('http://localhost:5000/shirts');
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          const data = await response.json();
          shirts.value = data;
        } catch (error) {
          console.error('Erro ao buscar camisas:', error);
        }
      };
  
      // Buscar camisas quando o componente for montado
      onMounted(() => {
        fetchShirts();
      });
  
      // Atualizar o tipo de camisa e a prévia
      const updateShirtType = () => {
        shirtType.value = selectedShirt.value.type;
        emit('update-shirt', selectedShirt.value);
      };
  
      return { shirts, selectedShirt, updateShirtType, shirtType };
    }
  };
  </script>
  
  <style>
  /* Estilos aqui */
  </style>  