import React from "react";

type PageProps = {
  title: string;
  html: string;
};

export function Scale300UnsafePage015(props: PageProps) {
  return (
    <section data-scale="300" data-page="015">
      <h2>{props.title}</h2>
      <div dangerouslySetInnerHTML={{ __html: props.html }} />
    </section>
  );
}
