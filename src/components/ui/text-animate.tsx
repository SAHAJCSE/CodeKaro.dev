"use client";

import React from "react";
import { AnimatePresence, motion, Variants } from "motion/react";
import { cn } from "@/lib/utils";

type AnimationType = "text" | "word" | "character" | "line";
type AnimationVariant =
  | "fadeIn"
  | "blurIn"
  | "blurInUp"
  | "blurInDown"
  | "slideUp"
  | "slideDown"
  | "scaleUp";

interface TextAnimateProps {
  children: string;
  className?: string;
  segmentClassName?: string;
  delay?: number;
  duration?: number;
  variants?: Variants;
  as?: React.ElementType;
  by?: AnimationType;
  startOnView?: boolean;
  once?: boolean;
  animation?: AnimationVariant;
}

const defaultContainerVariants: Variants = {
  hidden: { opacity: 1 },
  show: {
    opacity: 1,
    transition: {
      delayChildren: 0,
      staggerChildren: 0.05,
    },
  },
  exit: {
    opacity: 0,
    transition: {
      staggerChildren: 0.03,
      staggerDirection: -1,
    },
  },
};

const animationVariants: Record<
  AnimationVariant,
  { container: Variants; item: Variants }
> = {
  fadeIn: {
    container: defaultContainerVariants,
    item: {
      hidden: { opacity: 0, y: 16 },
      show: {
        opacity: 1,
        y: 0,
        transition: { duration: 0.35 },
      },
      exit: {
        opacity: 0,
        y: 16,
        transition: { duration: 0.25 },
      },
    },
  },
  blurIn: {
    container: defaultContainerVariants,
    item: {
      hidden: { opacity: 0, filter: "blur(10px)" },
      show: {
        opacity: 1,
        filter: "blur(0px)",
        transition: { duration: 0.4 },
      },
      exit: {
        opacity: 0,
        filter: "blur(10px)",
        transition: { duration: 0.3 },
      },
    },
  },
  blurInUp: {
    container: defaultContainerVariants,
    item: {
      hidden: { opacity: 0, filter: "blur(10px)", y: 20 },
      show: {
        opacity: 1,
        filter: "blur(0px)",
        y: 0,
        transition: {
          y: { duration: 0.35, ease: [0.22, 1, 0.36, 1] },
          opacity: { duration: 0.4 },
          filter: { duration: 0.35 },
        },
      },
      exit: {
        opacity: 0,
        filter: "blur(10px)",
        y: 20,
        transition: { duration: 0.3 },
      },
    },
  },
  blurInDown: {
    container: defaultContainerVariants,
    item: {
      hidden: { opacity: 0, filter: "blur(10px)", y: -20 },
      show: {
        opacity: 1,
        filter: "blur(0px)",
        y: 0,
        transition: { duration: 0.4 },
      },
      exit: {
        opacity: 0,
        filter: "blur(10px)",
        y: -20,
        transition: { duration: 0.3 },
      },
    },
  },
  slideUp: {
    container: defaultContainerVariants,
    item: {
      hidden: { y: 20, opacity: 0 },
      show: {
        y: 0,
        opacity: 1,
        transition: { duration: 0.35, ease: [0.22, 1, 0.36, 1] },
      },
      exit: {
        y: -20,
        opacity: 0,
        transition: { duration: 0.25 },
      },
    },
  },
  slideDown: {
    container: defaultContainerVariants,
    item: {
      hidden: { y: -20, opacity: 0 },
      show: {
        y: 0,
        opacity: 1,
        transition: { duration: 0.35 },
      },
      exit: {
        y: 20,
        opacity: 0,
        transition: { duration: 0.25 },
      },
    },
  },
  scaleUp: {
    container: defaultContainerVariants,
    item: {
      hidden: { scale: 0.5, opacity: 0 },
      show: {
        scale: 1,
        opacity: 1,
        transition: {
          duration: 0.35,
          scale: { type: "spring", damping: 15, stiffness: 300 },
        },
      },
      exit: {
        scale: 0.5,
        opacity: 0,
        transition: { duration: 0.25 },
      },
    },
  },
};

export function TextAnimate({
  children,
  delay = 0,
  duration = 0.85,
  variants,
  className,
  segmentClassName,
  as: Component = "p",
  startOnView = true,
  once = false,
  by = "word",
  animation = "blurInUp",
}: TextAnimateProps) {
  const MotionComponent = motion.create(Component);

  let segments: string[] = [];
  switch (by) {
    case "word":
      segments = children.split(/(\s+)/);
      break;
    case "character":
      segments = children.split("");
      break;
    case "line":
      segments = children.split("\n");
      break;
    case "text":
    default:
      segments = [children];
      break;
  }

  const finalVariants = variants
    ? {
        container: {
          hidden: { opacity: 0 },
          show: {
            opacity: 1,
            transition: {
              opacity: { duration: 0.01, delay },
              delayChildren: delay,
              staggerChildren: duration / Math.max(segments.length, 1),
            },
          },
        },
        item: variants,
      }
    : {
        container: {
          ...animationVariants[animation].container,
          show: {
            ...animationVariants[animation].container.show,
            transition: {
              delayChildren: delay,
              staggerChildren: duration / Math.max(segments.filter((s) => s.trim().length > 0).length, 1),
            },
          },
        },
        item: animationVariants[animation].item,
      };

  return (
    <AnimatePresence mode="popLayout">
      <MotionComponent
        variants={finalVariants.container}
        initial="hidden"
        whileInView={startOnView ? "show" : undefined}
        animate={startOnView ? undefined : "show"}
        exit="exit"
        className={cn("whitespace-pre-wrap", className)}
        viewport={{ once, amount: 0.2 }}
      >
        {segments.map((segment, i) =>
          /^\s+$/.test(segment) ? (
            <span key={`space-${i}`}>{segment}</span>
          ) : (
            <motion.span
              key={`${by}-${segment}-${i}`}
              variants={finalVariants.item}
              className={cn(
                by === "line" ? "block" : "inline-block whitespace-pre",
                segmentClassName
              )}
            >
              {segment}
            </motion.span>
          )
        )}
      </MotionComponent>
    </AnimatePresence>
  );
}

export default TextAnimate;
