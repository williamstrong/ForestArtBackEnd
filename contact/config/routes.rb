Rails.application.routes.draw do
  get 'contact/index'

  resources :contact

  root 'contact#index'
end
