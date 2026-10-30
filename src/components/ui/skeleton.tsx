"use client";

import React from "react";
import { cn } from "@/lib/utils";

export interface SkeletonProps extends React.HTMLAttributes<HTMLDivElement> {
  isLoaded?: boolean;
}

export function Skeleton({
  className,
  isLoaded = false,
  children,
  ...props
}: SkeletonProps) {
  if (isLoaded) {
    return <div className={cn("animate-fadeIn", className)}>{children}</div>;
  }

  return (
    <div
      data-slot="skeleton"
      className={cn(
        "heroui-skeleton relative overflow-hidden rounded-lg bg-muted/80",
        className
      )}
      {...props}
    >
      {children && <div className="invisible">{children}</div>}
    </div>
  );
}

export function Basic({ className }: { className?: string }) {
  return (
    <div
      className={cn(
        "shadow-panel w-[250px] space-y-5 rounded-lg bg-transparent p-4",
        className
      )}
    >
      <Skeleton className="h-32 rounded-lg" />
      <div className="space-y-3">
        <Skeleton className="h-3 w-3/5 rounded-lg" />
        <Skeleton className="h-3 w-4/5 rounded-lg" />
        <Skeleton className="h-3 w-2/5 rounded-lg" />
      </div>
    </div>
  );
}

export default Skeleton;
