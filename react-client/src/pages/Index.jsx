import { Link } from "react-router-dom";

const Index = () => {
   return (
      <div className="banner">
         <div className="container">
            <div className="row">
               <div className="col-lg-7 desc">
                  <h4 className="desc-title text-white d-flex"><div className="text-warning">Custo</div>mers</h4>
                  <p className="text-white mt-3">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960</p>
                  <Link className="btn btn-warning text-white mt-4" to="/customer">Learn More</Link>
               </div>
            </div>
         </div>
      </div>
   );
}

export default Index;