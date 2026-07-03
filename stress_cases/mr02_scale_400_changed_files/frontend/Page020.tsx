import React from "react";

type PageProps = {
  title: string;
  html: string;
};

export function Scale400UnsafePage020(props: PageProps) {
  return (
    <section data-scale="400" data-page="020">
      <h2>{props.title}</h2>
      <div dangerouslySetInnerHTML={{ __html: props.html }} />
    </section>
  );
}
