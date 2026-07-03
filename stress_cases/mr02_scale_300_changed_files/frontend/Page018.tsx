import React from "react";

type PageProps = {
  title: string;
  items: string[];
};

export function Scale300Page018(props: PageProps) {
  const visibleItems = props.items.filter((item) => item.trim().length > 0);
  return (
    <section data-scale="300" data-page="018">
      <h2>{props.title}</h2>
      <ul>
        {visibleItems.map((item) => (
          <li key={item}>{item}</li>
        ))}
      </ul>
    </section>
  );
}
