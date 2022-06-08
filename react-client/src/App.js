import { BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import './App.css';
import Navbar from './components/Navbar';
import Index from './pages/Index';
import Customer from './pages/Customer';
import CustomerAdd from './pages/CustomerAdd';
import CustomerDelete from './pages/CustomerDelete';
import CustomerUpdate from './pages/CustomerUpdate';

function App() {
  return (
    <Router>
    <Navbar />
      <Routes>
        <Route path="/" element={<Index />} />
        <Route path="/customers" element={<Customer />} />
        <Route path="/customers/add" element={<CustomerAdd />} />
        <Route path="/customers/delete/:id" element={<CustomerDelete />} />
        <Route path="/customers/edit/:id" element={<CustomerUpdate />} />
        <Route path="/about" element={''} />
        <Route path="*" element={<h1 className='text-center mt-5'>404 Not Found</h1>} />
      </Routes>
    </Router>
  );
}

export default App;
