import React from "react";

type PageProps = {
  title: string;
  items: string[];
};

export function Scale200Page008(props: PageProps) {
  const visibleItems = props.items.filter((item) => item.trim().length > 0);
  return (
    <section data-scale="200" data-page="008">
      <h2>{props.title}</h2>
      <ul>
        {visibleItems.map((item) => (
          <li key={item}>{item}</li>
        ))}
      </ul>
    </section>
  );
}
