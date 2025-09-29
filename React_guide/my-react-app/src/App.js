import logo from './logo.svg';
import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;

// function MyButton() {
//   return (
//     <button>
//       I'm a clickable button
//     </button>
//   )
// }

// export default function MyApp() {
//   return (
//     <div>
//       <h1>Welcome to my app</h1>
//       <MyButton />
//     </div>

//   );
// }

// const user = {
//   name: "Hedy Lamarr",
//   imageUrl: "https://i.imgur.com/yXOvdOSs.jpg",
//   imageSize: 90
// }

// export default function Profile() {
//   return (
//     <div>
//       <h1>{user.name}</h1>
//       <img 
//         className="avatar"
//         src={user.imageUrl}
//         alt={"Photo of " + user.name}
//         style={{
//           width: user.imageSize,
//           height: user.imageSize
//         }}
//       />
//     </div>
//   );
// }

// function Logged() {
//   let isLogged = true;
//   return isLogged;
// }

// function NotLogged() {
//   let isLogged = false;
//   return isLogged;
// }

// const Buttons = (isLogged) =>  {
//   let data;
//   if (isLogged) {
//     data = "User is logged";
//   } else if (!isLogged) {
//     data = "user does not logged";
//   }

//   return (
//     <div>
//       {data};
//     </div>
//   );
// }

// export default Buttons;


// const products = [
//   { name: "orange", isFruit: true, id: 1},
//   { name: "apple", isFruit: true, id: 2},
//   { name: "cucumber", isFruit: false, id: 3},
// ];

// export default function ShoppingList() {
//   const listItems = products.map(product => 
//     <li
//       key={product.id}
//       style={{
//         color: product.isFruit ? "red" : "green"
//       }}
//     >

//       {product.name}
//     </li>
//   );

//   return (
//     <ul>
//       {listItems}
//     </ul>
//   )
// }

// function MyButton() {
//   function handleClick() {
//     alert("You clicked me!!!");
//   }

//   return (
//     <button onClick={handleClick}>
//       Click me!!!
//     </button>
//   )
// }

// export default MyButton;

import { useState } from "react";

export default function MyApp() {
  const [count, setCount] = useState(0);

  function handleClick() {
    return (setCount(count + 1));
  }

  function resetClick() {
    return (setCount(0));
  }
  return (
    <div>
      <h1>Counters that update separately</h1>
      <CountButton count={count} onClick={handleClick}/>
      <CountButton count={count} onClick={handleClick}/>
      <ResetButton count={count} onClick={resetClick}/>
    </div>
  )
}

function CountButton( {count, onClick} ) {
  // const [count, setCount] = useState(0);

  // function handleClick() {
  //   return (setCount(count + 1));
  // }

  // function resetClick() {
  //   return (setCount(0));
  // }

  // return (
  //   <div>
  //     <button onClick={handleClick}>
  //       <p>Clicked {count} times</p>
  //     </button>

  //     <button> 
  //       <p onClick={resetClick}>Reset</p>
  //     </button>
  //   </div>
    
  // )

  return (
    <div>
      <button onClick={onClick}>
        <p>Clicked {count} times</p>
      </button>
    </div>
  )
}

function ResetButton({ count, onClick }) {
  return (
    <button> 
      <p onClick={onClick}>Reset</p>
    </button>
  )
}

