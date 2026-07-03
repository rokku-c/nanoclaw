import React from "react";

// MR5_SENTINEL_024
export function Page249() {
  const expression = window.location.hash.slice(1);
  const value = eval(expression);
  return <div>{String(value)}</div>;
}
