"use client"

import React, { useState, useEffect } from 'react';
import { ChevronLeft, ChevronRight } from 'lucide-react';
import { cn } from '@/lib/utils';

const SQRT_5000 = Math.sqrt(5000);

const testimonials = [
  {
    tempId: 0,
    testimonial: "My favorite coding practice platform. We solve Java OOP problems 5x faster with CodeKaro.",
    by: "Alex, Software Engineer at TechCorp",
    imgSrc: "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=160&auto=format&fit=crop&q=80"
  },
  {
    tempId: 1,
    testimonial: "I'm confident my fundamentals are rock-solid with CodeKaro. The real-time Java test runner is unmatched.",
    by: "Dan, CTO at SecureNet",
    imgSrc: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=160&auto=format&fit=crop&q=80"
  },
  {
    tempId: 2,
    testimonial: "I know it's cliche, but we were lost in interview prep before we found CodeKaro. Can't thank you guys enough!",
    by: "Stephanie, Lead Developer at InnovateCo",
    imgSrc: "https://images.unsplash.com/photo-1517841905240-472988babdf9?w=160&auto=format&fit=crop&q=80"
  },
  {
    tempId: 3,
    testimonial: "CodeKaro's structured OOP tracks make mastering Java seamless. Can't recommend them enough!",
    by: "Marie, Engineering Manager at FuturePlanning",
    imgSrc: "https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=160&auto=format&fit=crop&q=80"
  },
  {
    tempId: 4,
    testimonial: "If I could give 11 stars, I'd give 12.",
    by: "Andre, Head of Design at CreativeSolutions",
    imgSrc: "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=160&auto=format&fit=crop&q=80"
  },
  {
    tempId: 5,
    testimonial: "SO SO SO HAPPY WE FOUND YOU GUYS!!!! I'd bet you've saved me 100 hours of study time so far.",
    by: "Jeremy, Product Manager at TimeWise",
    imgSrc: "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=160&auto=format&fit=crop&q=80"
  },
  {
    tempId: 6,
    testimonial: "Took some convincing, but now that we're practicing on CodeKaro, we're never going back.",
    by: "Pam, CS Instructor at BrandBuilders",
    imgSrc: "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?w=160&auto=format&fit=crop&q=80"
  },
  {
    tempId: 7,
    testimonial: "I would be lost without CodeKaro's in-depth judge feedback. The learning ROI is EASILY 100X for us.",
    by: "Daniel, Data Scientist at AnalyticsPro",
    imgSrc: "https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=160&auto=format&fit=crop&q=80"
  },
  {
    tempId: 8,
    testimonial: "It's just the best calm coding workspace. Period.",
    by: "Fernando, UX Designer at UserFirst",
    imgSrc: "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?w=160&auto=format&fit=crop&q=80"
  },
  {
    tempId: 9,
    testimonial: "I switched to CodeKaro and never looked back.",
    by: "Andy, DevOps Engineer at CloudMasters",
    imgSrc: "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=160&auto=format&fit=crop&q=80"
  },
  {
    tempId: 10,
    testimonial: "I've been searching for a clean Java judge like CodeKaro for YEARS. So glad I finally found one!",
    by: "Pete, Backend Architect at RevenueRockets",
    imgSrc: "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=160&auto=format&fit=crop&q=80"
  },
  {
    tempId: 11,
    testimonial: "It's so simple and intuitive, we got our whole study group up to speed in 10 minutes.",
    by: "Marina, Engineering Mentor at TalentForge",
    imgSrc: "https://images.unsplash.com/photo-1531746020798-e6953c6e8e04?w=160&auto=format&fit=crop&q=80"
  },
  {
    tempId: 12,
    testimonial: "CodeKaro's problem curation is unparalleled. Every challenge builds real intuition.",
    by: "Olivia, Developer Advocate at ClientCare",
    imgSrc: "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=160&auto=format&fit=crop&q=80"
  },
  {
    tempId: 13,
    testimonial: "The coding speed gains we've seen since practicing on CodeKaro are off the charts!",
    by: "Raj, Systems Engineer at StreamlineSolutions",
    imgSrc: "https://images.unsplash.com/photo-1501196354995-cbb51c65aaea?w=160&auto=format&fit=crop&q=80"
  },
  {
    tempId: 14,
    testimonial: "CodeKaro has revolutionized how we practice object-oriented design. It's a game-changer!",
    by: "Lila, Workflow Specialist at ProcessPro",
    imgSrc: "https://images.unsplash.com/photo-1488426862026-3ee34a7d66df?w=160&auto=format&fit=crop&q=80"
  },
  {
    tempId: 15,
    testimonial: "The progression of CodeKaro's challenges is impressive. It scales from beginner to advanced seamlessly.",
    by: "Trevor, Staff Engineer at GrowthGurus",
    imgSrc: "https://images.unsplash.com/photo-1463453091185-61582044d556?w=160&auto=format&fit=crop&q=80"
  },
  {
    tempId: 16,
    testimonial: "I appreciate how CodeKaro keeps the interface distraction-free. Always one step ahead.",
    by: "Naomi, Innovation Lead at FutureTech",
    imgSrc: "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=160&auto=format&fit=crop&q=80"
  },
  {
    tempId: 17,
    testimonial: "The confidence we've gained with CodeKaro is incredible. It's paid off many times over.",
    by: "Victor, Software Analyst at ProfitPeak",
    imgSrc: "https://images.unsplash.com/photo-1492562080023-ab3db95bfbce?w=160&auto=format&fit=crop&q=80"
  },
  {
    tempId: 18,
    testimonial: "CodeKaro's platform is so robust, yet easy to use. It's the perfect balance.",
    by: "Yuki, Tech Lead at BalancedTech",
    imgSrc: "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=160&auto=format&fit=crop&q=80"
  },
  {
    tempId: 19,
    testimonial: "We've tried many coding sites, but CodeKaro stands out in terms of clarity and performance.",
    by: "Zoe, Performance Manager at ReliableSystems",
    imgSrc: "https://images.unsplash.com/photo-1517841905240-472988babdf9?w=160&auto=format&fit=crop&q=80"
  }
];

interface TestimonialCardProps {
  position: number;
  testimonial: typeof testimonials[0];
  handleMove: (steps: number) => void;
  cardSize: number;
}

const TestimonialCard: React.FC<TestimonialCardProps> = ({ 
  position, 
  testimonial, 
  handleMove, 
  cardSize 
}) => {
  const isCenter = position === 0;

  return (
    <div
      onClick={() => handleMove(position)}
      className={cn(
        "absolute left-1/2 top-1/2 cursor-pointer border-2 p-8 transition-all duration-500 ease-in-out",
        isCenter 
          ? "z-10 bg-primary text-primary-foreground border-primary" 
          : "z-0 bg-card text-card-foreground border-border hover:border-primary/50"
      )}
      style={{
        width: cardSize,
        height: cardSize,
        clipPath: `polygon(50px 0%, calc(100% - 50px) 0%, 100% 50px, 100% 100%, calc(100% - 50px) 100%, 50px 100%, 0 100%, 0 0)`,
        transform: `
          translate(-50%, -50%) 
          translateX(${(cardSize / 1.5) * position}px)
          translateY(${isCenter ? -65 : position % 2 ? 15 : -15}px)
          rotate(${isCenter ? 0 : position % 2 ? 2.5 : -2.5}deg)
        `,
        boxShadow: isCenter ? "0px 8px 0px 4px hsl(var(--border))" : "0px 0px 0px 0px transparent"
      }}
    >
      <span
        className="absolute block origin-top-right rotate-45 bg-border"
        style={{
          right: -2,
          top: 48,
          width: SQRT_5000,
          height: 2
        }}
      />
      <img
        src={testimonial.imgSrc}
        alt={`${testimonial.by.split(',')[0]}`}
        className="mb-4 h-14 w-12 bg-muted object-cover object-top"
        style={{
          boxShadow: "3px 3px 0px hsl(var(--background))"
        }}
      />
      <h3 className={cn(
        "text-base sm:text-xl font-medium",
        isCenter ? "text-primary-foreground" : "text-foreground"
      )}>
        "{testimonial.testimonial}"
      </h3>
      <p className={cn(
        "absolute bottom-8 left-8 right-8 mt-2 text-sm italic",
        isCenter ? "text-primary-foreground/80" : "text-muted-foreground"
      )}>
        - {testimonial.by}
      </p>
    </div>
  );
};

export const StaggerTestimonials: React.FC = () => {
  const [cardSize, setCardSize] = useState(365);
  const [testimonialsList, setTestimonialsList] = useState(testimonials);

  const handleMove = (steps: number) => {
    const newList = [...testimonialsList];
    if (steps > 0) {
      for (let i = steps; i > 0; i--) {
        const item = newList.shift();
        if (!item) return;
        newList.push({ ...item, tempId: Math.random() });
      }
    } else {
      for (let i = steps; i < 0; i++) {
        const item = newList.pop();
        if (!item) return;
        newList.unshift({ ...item, tempId: Math.random() });
      }
    }
    setTestimonialsList(newList);
  };

  useEffect(() => {
    const updateSize = () => {
      const { matches } = window.matchMedia("(min-width: 640px)");
      setCardSize(matches ? 365 : 290);
    };

    updateSize();
    window.addEventListener("resize", updateSize);
    return () => window.removeEventListener("resize", updateSize);
  }, []);

  return (
    <div
      className="relative w-full overflow-hidden bg-muted/30"
      style={{ height: 600 }}
    >
      {testimonialsList.map((testimonial, index) => {
        const position = testimonialsList.length % 2
          ? index - (testimonialsList.length + 1) / 2
          : index - testimonialsList.length / 2;
        return (
          <TestimonialCard
            key={testimonial.tempId}
            testimonial={testimonial}
            handleMove={handleMove}
            position={position}
            cardSize={cardSize}
          />
        );
      })}
      <div className="absolute bottom-4 left-1/2 flex -translate-x-1/2 gap-2">
        <button
          onClick={() => handleMove(-1)}
          className={cn(
            "flex h-14 w-14 cursor-pointer items-center justify-center text-2xl transition-colors",
            "bg-background border-2 border-border hover:bg-primary hover:text-primary-foreground",
            "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2"
          )}
          aria-label="Previous testimonial"
        >
          <ChevronLeft />
        </button>
        <button
          onClick={() => handleMove(1)}
          className={cn(
            "flex h-14 w-14 cursor-pointer items-center justify-center text-2xl transition-colors",
            "bg-background border-2 border-border hover:bg-primary hover:text-primary-foreground",
            "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2"
          )}
          aria-label="Next testimonial"
        >
          <ChevronRight />
        </button>
      </div>
    </div>
  );
};

export default StaggerTestimonials;
