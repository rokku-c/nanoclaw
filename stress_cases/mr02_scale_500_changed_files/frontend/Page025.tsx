import React from "react";

type PageProps = {
  title: string;
  html: string;
};

export function Scale500UnsafePage025(props: PageProps) {
  return (
    <section data-scale="500" data-page="025">
      <h2>{props.title}</h2>
      <div dangerouslySetInnerHTML={{ __html: props.html }} />
    </section>
  );
}
