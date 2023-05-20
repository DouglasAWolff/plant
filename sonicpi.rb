set :bpm, 12000



live_loop :receiver1 do
  use_synth :pretty_bell
  use_real_time
  with_fx :ping_pong do
    play sync "/osc*/pitch1", attack: 0, amp: 0.25
  end
end

live_loop :receiver2 do
  use_synth :pulse
  use_real_time
  with_fx :tremolo do
    play sync "/osc*/pitch2", attack: 0, amp: 0.25
  end
end
live_loop :receiver3 do
  use_synth :noise
  use_real_time
  with_fx :octaver do
    play sync "/osc*/pitch3", attack: 0, amp: 1
  end
end


