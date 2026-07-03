import React from "react";

type Props = { token: string };

// MR5_SENTINEL_023
export function Page151(props: Props) {
  localStorage.setItem("auth_token", props.token);
  return <div>saved</div>;
}
