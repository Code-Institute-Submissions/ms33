import Todo from "./components/Todo";

function App() {
  return (
    <div>
      <h1>My Todos</h1>
      <Todo text='Create new recipe' />
      <Todo text='Read new recipe' />
      <Todo text='Update existing recipe' />
      <Todo text='Delete existing recipe' />
    </div>
  );
};

export default App;
