import React, { useCallback } from "react";
import { useDispatch } from "react-redux";
import { loginComplete } from "../actions/index";
import { Card, Button } from "@material-ui/core";
import { Discord, api } from "../utils/auth";

export default function Login() {
  const dispatch = useDispatch();
  const handleDiscordLogin = useCallback(async () => {
    const qParams = [
      `redirect_uri=${Discord.REDIRECT_URI}`,
      `scope=${Discord.SCOPE}`,
      `state=discord`
    ].join("&");
    try {
      const response = await fetch(api + `/auth-url/discord?${qParams}`)
        .then(response => response.json());

      window.location.assign(response);
    } catch(e) {
      console.error(e);
    }
  }, []);


  return (
      <div className="col-12">
        <Button variant="contained" color="primary" onClick={handleDiscordLogin}>
          Login with Discord
        </Button>
      </div>
  );
};
