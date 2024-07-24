<template>
    <div class="selector">
      <h2>Escolha a Cor</h2>
      <select v-model="selectedColor">
        <option v-for="color in colors" :key="color.id" :value="color">{{ color.name }}</option>
      </select>
    </div>
  </template>
  
  <script>
  import { ref, watch } from 'vue';
  
  export default {
    props: {
      shirtType: {
        type: String,
        required: true
      }
    },
    setup(props) {
      const colors = ref([]);
      const selectedColor = ref(null);
  
      // Função para buscar cores da API com base no tipo de camisa
      const fetchColors = async () => {
        try {
          const response = await fetch(`http://localhost:5000/colors?shirt_type=${props.shirtType}`);
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          const data = await response.json();
          colors.value = data;
        } catch (error) {
          console.error('Erro ao buscar cores:', error);
        }
      };
  
      // Observar mudanças no tipo de camisa e atualizar as cores
      watch(() => props.shirtType, fetchColors, { immediate: true });
  
      return { colors, selectedColor };
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