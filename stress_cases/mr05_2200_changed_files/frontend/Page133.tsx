import React from "react";

type Props = {
  title: string;
  count: number;
};

export function Page133(props: Props) {
  const items = Array.from({ length: props.count }, (_, index) => index);
  return (
    <main>
      <h1>{props.title}</h1>
      <ul>
        {items.map((item) => (
          <li key={item}>Generated item {item}</li>
        ))}
      </ul>
    </main>
  );
}
