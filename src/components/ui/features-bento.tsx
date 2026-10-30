import React from "react";
import { BentoCard, BentoGrid } from "@/components/ui/bento-grid";
import { TextAnimate } from "@/components/ui/text-animate";

const JavaPreview = () => (
  <div className="pointer-events-none absolute inset-x-5 top-5 rounded-xl border border-white/15 bg-[#121215] p-4 font-mono text-xs text-zinc-300 shadow-sm transition-all duration-300 group-hover:border-white/30 [[data-theme=light]_&]:border-black/12 [[data-theme=light]_&]:bg-zinc-50 [[data-theme=light]_&]:text-zinc-800 [[data-theme=light]_&]:group-hover:border-black/25">
    <div className="mb-2 flex items-center gap-1.5">
      <span className="h-2.5 w-2.5 rounded-full bg-zinc-600 [[data-theme=light]_&]:bg-zinc-300" />
      <span className="h-2.5 w-2.5 rounded-full bg-zinc-500 [[data-theme=light]_&]:bg-zinc-400" />
      <span className="h-2.5 w-2.5 rounded-full bg-zinc-400 [[data-theme=light]_&]:bg-zinc-500" />
      <span className="ml-2 text-[11px] text-zinc-400 [[data-theme=light]_&]:text-zinc-500">Solution.java</span>
    </div>
    <pre className="overflow-hidden leading-relaxed">
      <span className="font-semibold text-white [[data-theme=light]_&]:text-black">public class</span>{" "}
      <span className="underline decoration-zinc-500/50 underline-offset-2">BankAccount</span> {"{\n"}
      {"  "}
      <span className="font-semibold text-white [[data-theme=light]_&]:text-black">private double</span> balance;{"\n"}
      {"  "}
      <span className="font-semibold text-white [[data-theme=light]_&]:text-black">public void</span>{" "}
      <span className="font-medium">deposit</span>(double amt) {"{\n"}
      {"    "}if (amt &gt; 0) balance += amt;{"\n"}
      {"  }\n}"}
    </pre>
  </div>
);

const TestsPreview = () => (
  <div className="pointer-events-none absolute inset-x-5 top-5 flex flex-col gap-2.5">
    {[
      { label: "Test 01 · Inheritance Hierarchy", ms: "12 ms" },
      { label: "Test 02 · Polymorphic Dispatch", ms: "18 ms" },
      { label: "Test 03 · Encapsulation Guards", ms: "9 ms" },
    ].map((t) => (
      <div
        key={t.label}
        className="flex items-center justify-between rounded-lg border border-white/15 bg-[#121215] px-3.5 py-2.5 text-xs transition-all duration-300 group-hover:translate-x-1 [[data-theme=light]_&]:border-black/12 [[data-theme=light]_&]:bg-zinc-50"
      >
        <span className="flex items-center gap-2 font-medium text-zinc-100 [[data-theme=light]_&]:text-zinc-900">
          <span className="h-2 w-2 rounded-full bg-white [[data-theme=light]_&]:bg-black" />
          {t.label}
        </span>
        <span className="font-mono text-[11px] text-zinc-400 [[data-theme=light]_&]:text-zinc-600">{t.ms}</span>
      </div>
    ))}
  </div>
);

const SkylinePreview = () => (
  <div className="pointer-events-none absolute inset-x-5 top-6 flex h-32 items-end justify-between gap-2 rounded-xl border border-white/15 bg-[#121215] p-4 [[data-theme=light]_&]:border-black/12 [[data-theme=light]_&]:bg-zinc-50">
    {[35, 60, 45, 85, 55, 95, 70, 40, 80, 100, 65, 90].map((h, idx) => (
      <div
        key={idx}
        style={{ height: `${h}%` }}
        className="w-full rounded-t-sm bg-white/80 transition-all duration-300 group-hover:bg-white [[data-theme=light]_&]:bg-black/75 [[data-theme=light]_&]:group-hover:bg-black"
      />
    ))}
  </div>
);

const ProgressPreview = () => (
  <div className="pointer-events-none absolute inset-x-5 top-5 flex flex-col gap-3 rounded-xl border border-white/15 bg-[#121215] p-4 [[data-theme=light]_&]:border-black/12 [[data-theme=light]_&]:bg-zinc-50">
    {[
      { topic: "Classes & Objects", pct: 92 },
      { topic: "Inheritance & Interfaces", pct: 78 },
      { topic: "Collections & Generics", pct: 64 },
    ].map((item) => (
      <div key={item.topic} className="space-y-1.5">
        <div className="flex justify-between text-xs">
          <span className="font-medium text-zinc-100 [[data-theme=light]_&]:text-zinc-900">{item.topic}</span>
          <span className="font-mono text-zinc-400 [[data-theme=light]_&]:text-zinc-600">{item.pct}%</span>
        </div>
        <div className="h-1.5 w-full overflow-hidden rounded-full bg-white/15 [[data-theme=light]_&]:bg-black/10">
          <div
            style={{ width: `${item.pct}%` }}
            className="h-full rounded-full bg-white transition-all duration-500 [[data-theme=light]_&]:bg-black"
          />
        </div>
      </div>
    ))}
  </div>
);

const features = [
  {
    name: "Write Real Java Code",
    description:
      "Practice object-oriented Java in a distraction-free browser IDE with syntax highlighting and starter templates.",
    href: "/practice",
    cta: "Open Editor",
    background: <JavaPreview />,
    className: "md:col-span-2",
  },
  {
    name: "Instant Test Suites",
    description:
      "Execute your solution against real unit tests with millisecond runtime feedback and clear diffs.",
    href: "/practice",
    cta: "Run Tests",
    background: <TestsPreview />,
    className: "md:col-span-1",
  },
  {
    name: "Contribution Skyline",
    description:
      "Visualize your daily coding streak in an interactive 2D heatmap or 3D isometric skyline.",
    href: "/dashboard",
    cta: "View Dashboard",
    background: <SkylinePreview />,
    className: "md:col-span-1",
  },
  {
    name: "Structured OOP Mastery",
    description:
      "Turn every solved challenge into measurable progress across encapsulation, inheritance, polymorphism, and abstraction.",
    href: "/dashboard",
    cta: "Track Progress",
    background: <ProgressPreview />,
    className: "md:col-span-2",
  },
];

export function FeaturesBentoSection() {
  return (
    <section
      aria-label="Platform features"
      className="w-full bg-[#09090b] px-6 py-20 text-[#fafafa] transition-colors [[data-theme=light]_&]:bg-white [[data-theme=light]_&]:text-[#09090b] sm:px-10 lg:px-20"
    >
      <div className="mx-auto flex max-w-6xl flex-col items-center">
        <div className="mb-14 flex max-w-4xl flex-col items-center text-center">
          <span className="mb-4 inline-flex items-center gap-2.5 font-mono text-[11px] font-semibold uppercase tracking-[0.2em] text-zinc-400 [[data-theme=light]_&]:text-zinc-600">
            <span className="h-px w-5 bg-current" />
            Practice Java
            <span className="h-px w-5 bg-current" />
          </span>

          <TextAnimate
            as="h2"
            by="word"
            animation="blurInUp"
            className="text-center text-2xl font-bold leading-snug tracking-tight text-current sm:text-4xl md:text-[2.5rem] md:leading-[1.22]"
          >
            Learn Java by writing it. Solve focused programming challenges, run your code against real tests, and turn each problem into progress.
          </TextAnimate>
        </div>

        <BentoGrid className="w-full">
          {features.map((feature) => (
            <BentoCard key={feature.name} {...feature} />
          ))}
        </BentoGrid>
      </div>
    </section>
  );
}

export const FeaturesBento = FeaturesBentoSection;
export default FeaturesBentoSection;
