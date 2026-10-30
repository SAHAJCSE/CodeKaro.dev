import React, { createContext, useContext, useState } from "react";
import { ChevronDown } from "lucide-react";
import { cn } from "@/lib/utils";

interface AccordionContextValue {
  openIndex: number | null;
  toggleItem: (index: number) => void;
  variant?: "surface" | "default";
}

const AccordionContext = createContext<AccordionContextValue>({
  openIndex: 0,
  toggleItem: () => {},
  variant: "surface",
});

const AccordionItemContext = createContext<{ index: number; isOpen: boolean }>({
  index: 0,
  isOpen: false,
});

interface AccordionProps extends React.HTMLAttributes<HTMLDivElement> {
  variant?: "surface" | "default";
  defaultOpenIndex?: number | null;
}

function AccordionRoot({
  children,
  className,
  variant = "surface",
  defaultOpenIndex = 0,
  ...props
}: AccordionProps) {
  const [openIndex, setOpenIndex] = useState<number | null>(defaultOpenIndex);

  const toggleItem = (index: number) => {
    setOpenIndex((prev) => (prev === index ? null : index));
  };

  return (
    <AccordionContext.Provider value={{ openIndex, toggleItem, variant }}>
      <div
        className={cn(
          "flex flex-col gap-3",
          variant === "surface" && "w-full",
          className
        )}
        {...props}
      >
        {React.Children.map(children, (child, idx) => {
          if (!React.isValidElement(child)) return child;
          const isOpen = openIndex === idx;
          return (
            <AccordionItemContext.Provider value={{ index: idx, isOpen }}>
              {child}
            </AccordionItemContext.Provider>
          );
        })}
      </div>
    </AccordionContext.Provider>
  );
}

function AccordionItem({
  children,
  className,
  ...props
}: React.HTMLAttributes<HTMLDivElement>) {
  const { isOpen } = useContext(AccordionItemContext);
  return (
    <div
      data-open={isOpen ? "true" : "false"}
      className={cn(
        "overflow-hidden rounded-xl border border-white/15 bg-[#0a0a0c] text-[#fafafa] transition-all duration-200",
        "[[data-theme=light]_&]:border-black/12 [[data-theme=light]_&]:bg-white [[data-theme=light]_&]:text-[#09090b]",
        isOpen
          ? "border-white/35 [[data-theme=light]_&]:border-black/35"
          : "hover:border-white/25 [[data-theme=light]_&]:hover:border-black/25",
        className
      )}
      {...props}
    >
      {children}
    </div>
  );
}

function AccordionHeading({
  children,
  className,
  ...props
}: React.HTMLAttributes<HTMLHeadingElement>) {
  return (
    <h3 className={cn("m-0 flex", className)} {...props}>
      {children}
    </h3>
  );
}

function AccordionTrigger({
  children,
  className,
  ...props
}: React.ButtonHTMLAttributes<HTMLButtonElement>) {
  const { toggleItem } = useContext(AccordionContext);
  const { index, isOpen } = useContext(AccordionItemContext);

  return (
    <button
      type="button"
      aria-expanded={isOpen}
      onClick={() => toggleItem(index)}
      className={cn(
        "flex w-full cursor-pointer items-center justify-between gap-4 px-5 py-4 text-left text-base font-semibold text-current transition-colors",
        className
      )}
      {...props}
    >
      <span className="flex items-center text-base font-medium leading-snug">
        {children}
      </span>
    </button>
  );
}

function AccordionIndicator({
  children,
  className,
  ...props
}: React.HTMLAttributes<HTMLSpanElement>) {
  const { isOpen } = useContext(AccordionItemContext);
  return (
    <span
      className={cn(
        "ml-auto flex size-5 shrink-0 items-center justify-center text-zinc-400 transition-transform duration-200 [[data-theme=light]_&]:text-zinc-600",
        isOpen && "rotate-180 text-white [[data-theme=light]_&]:text-black",
        className
      )}
      {...props}
    >
      {children}
    </span>
  );
}

function AccordionPanel({
  children,
  className,
  ...props
}: React.HTMLAttributes<HTMLDivElement>) {
  const { isOpen } = useContext(AccordionItemContext);
  if (!isOpen) return null;
  return (
    <div
      className={cn(
        "border-t border-white/10 px-5 pb-4 pt-3 text-base leading-relaxed text-zinc-400 [[data-theme=light]_&]:border-black/10 [[data-theme=light]_&]:text-zinc-600",
        className
      )}
      {...props}
    >
      {children}
    </div>
  );
}

function AccordionBody({
  children,
  className,
  ...props
}: React.HTMLAttributes<HTMLDivElement>) {
  return (
    <div className={cn("text-[15px] leading-relaxed", className)} {...props}>
      {children}
    </div>
  );
}

export const Accordion = Object.assign(AccordionRoot, {
  Item: AccordionItem,
  Heading: AccordionHeading,
  Trigger: AccordionTrigger,
  Indicator: AccordionIndicator,
  Panel: AccordionPanel,
  Body: AccordionBody,
});

const items = [
  {
    title: "How do I start solving Java problems on CodeKaro?",
    content:
      "Open the Practice Editor, select any object-oriented Java challenge from the problem list, write your solution in the browser IDE, and click Run Code to test against real unit test cases immediately.",
  },
  {
    title: "How does the automated Java judge evaluate my code?",
    content:
      "Every submission is compiled and executed against structured unit and edge-case test suites. You receive instant verdict badges, execution runtime in milliseconds, and detailed expected-vs-actual diffs.",
  },
  {
    title: "Is CodeKaro completely free for students and developers?",
    content:
      "Yes. All Java OOP tracks, interactive test suites, the 3D Contribution Skyline, and progress analytics are completely free and open-source.",
  },
  {
    title: "What Java OOP topics and challenges are included?",
    content:
      "Challenges cover classes and objects, encapsulation, inheritance hierarchies, polymorphism, abstract classes and interfaces, matrix transformations, and thread-safe concurrency patterns.",
  },
  {
    title: "Can I access my coding streak and progress from any device?",
    content:
      "Yes. Sign in with Google, GitHub, or Email OTP to sync your solved problems, daily practice streak, and submission history across browsers.",
  },
  {
    title: "Can I reset my starter code or retry a solved challenge?",
    content:
      "You can reset the editor back to the clean Java starter template at any time and submit multiple solutions to compare runtime efficiency.",
  },
];

export function Surface() {
  return (
    <Accordion className="w-full max-w-3xl" variant="surface">
      {items.map((item, index) => (
        <Accordion.Item key={index}>
          <Accordion.Heading>
            <Accordion.Trigger>
              {item.title}
              <Accordion.Indicator>
                <ChevronDown className="size-4" />
              </Accordion.Indicator>
            </Accordion.Trigger>
          </Accordion.Heading>
          <Accordion.Panel>
            <Accordion.Body>{item.content}</Accordion.Body>
          </Accordion.Panel>
        </Accordion.Item>
      ))}
    </Accordion>
  );
}

export function FaqSection() {
  return (
    <section
      aria-label="Frequently Asked Questions"
      className="w-full bg-[#09090b] px-6 py-20 text-[#fafafa] transition-colors [[data-theme=light]_&]:bg-white [[data-theme=light]_&]:text-[#09090b] sm:px-10 lg:px-20"
    >
      <div className="mx-auto flex max-w-4xl flex-col items-center">
        <div className="mb-10 flex max-w-2xl flex-col items-center text-center">
          <span className="mb-3 inline-flex items-center gap-2.5 font-mono text-[11px] font-semibold uppercase tracking-[0.2em] text-zinc-400 [[data-theme=light]_&]:text-zinc-600">
            <span className="h-px w-5 bg-current" />
            FAQ
            <span className="h-px w-5 bg-current" />
          </span>
          <h2 className="text-center text-2xl font-bold tracking-tight text-current sm:text-4xl">
            Frequently Asked Questions
          </h2>
        </div>
        <Surface />
      </div>
    </section>
  );
}
