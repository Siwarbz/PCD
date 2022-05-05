import React from 'react';
import HeroSection from '../../HeroSection';
import { homeObjOne, homeObjTwo, homeObjThree, homeObjFour } from './Data';
import Pricing from '../../Pricing';

function Services() {
  
  return (
    <section id='services'>
    
      
      <HeroSection {...homeObjTwo} />
    
    </section>
  );
}

export default Services;