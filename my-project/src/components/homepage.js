import { LockClosedIcon } from '@heroicons/react/solid'
import logo from '../images/logo.png'
export default function homepage() {
  return (
    <>
      
         {/* This example requires updating your template: */}

        
        {/* <html class="h-full bg-gray-50">
        <body class="h-full"> */}
        
      
     {/* <div style={{ 
      backgroundImage: `url("https://st1.photogallery.ind.sh/wp-content/uploads/indiacom/sunny-leone-sets-gram-on-fire-202112-1638531570.jpg")`,
      backgroundSize:"contain" ,
      backgroundRepeat:"no-repeat",
      height: 600,
      width : 600
    }}>
      </div> */}
       <div style={{ 
      backgroundImage: `url("https://d3d343oddxxyuu.cloudfront.net/images/chapters/iEvf14FAMEDA6oH7e0l1Nqy369vCgwBvX4dPK5mD.png")`,
      backgroundSize:"cover" ,
      backgroundRepeat:"no-repeat",
      backgroundPosition: "center",
      height: '100%',

      width: '100%',
      position: 'fixed',
    }}
    >
      <nav >
        <div >
        <img
              className="object-left h-12 w-auto mx-4 my-4"
              src={logo}
              alt="logo"
            />
        </div>
        </nav>
      <div className="min-h-screen flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
     
      </div>
      </div>
    </>
  )
}